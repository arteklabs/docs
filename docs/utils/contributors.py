"""Gets the commit count for the projects contributors.
"""
import subprocess
import pandas as pd
import matplotlib


def get_commit_count():
    """Get all project's contributors commit count accross all remote branches, excluding merges."""
    command = "git shortlog -sne --no-merges --all --numstat"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.split("\n")


# Parse the command output and create a DataFrame
output_lines = get_commit_count()
data = [line.lower().split("\t") for line in output_lines]
data = [["commits", "user"]] + data
df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row contains column names

# clean names
df = df.apply(lambda x: x.str.replace("á", "a") if x.dtype == "object" else x)

# split user field into name and email
df[["user.name", "user.email"]] = df["user"].str.split(" <", expand=True)

# include only what is inside paranthesis, if there are parenthesis
df["user.name"] = df["user.name"].str.extract(r"\((.*)\)", expand=False).fillna(df["user.name"])

# remove trailing >
df["user.email"] = df["user.email"].str.replace(">", "")

# remove null rows
df.dropna(inplace=True)

# remove duplicate emails
df["user.email"] = df["user.email"].apply(lambda x: ", ".join(set(x.split(", "))))

# aggregate on user and concat emails and sum commits
df = df.groupby("user.name").agg({"user.email": lambda x: ", ".join(x), "commits": "sum"}).reset_index()

# commits replace multiple spaces with a single , and then split on ,
df["commits"] = df["commits"].str.replace("\s+", ",", regex=True).str.split(",")

# commits sum the list of strings
df["commits"] = df["commits"].apply(lambda x: sum([int(i) for i in x if i != ""]))

# order by name
df = df.sort_values(by=["user.name"])

# plot the results into svg
matplotlib.use("svg")
df.plot(kind="barh", x="user.name", y="commits", figsize=(10, 10), legend=True)
matplotlib.pyplot.savefig("../sphinx/static/img/contributors.svg")

# print user.name and user.email to html table
df[["user.name", "user.email"]].to_html("../sphinx/static/img/contributors.html", index=False)
