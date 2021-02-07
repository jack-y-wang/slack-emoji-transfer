# Slack Workspace Emoji Transfer

A way to bulk move slack emojis from workspace to another.
_NOTE_: this will require having admin access on the source slack workspace and priviledges to create custom emojis on the destination slack workspace.

## Steps

#### Step 1

- Obtain a JSON of the emoji list of your source workpsace by going to https://api.slack.com/methods/emoji.list/test and inputting your user token (make sure that you're an admin for this workspace)
- Copy the `emoji` object into the file `emoji.json`
- Run the Python Script with the following steps which should create the img and gif files of all the emojis in a emoji/ folder:
  1. Create a virtual environment `pip -m venv venv`
  2. Activate the virtual environment `source ./venv/bin/activate`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Run the python script with `python script.py`

#### Step 2

Go to this [slack emoji uploader repo](https://github.com/sgreben/slack-emoji-upload) and use it to upload the emojis to the destination workspace; below are the following steps that I found to work best

- Download the binary from the [latest release](https://github.com/sgreben/slack-emoji-upload/releases/latest)
- Open the zip file
- In the current directory where you ran the `script.py` file
- Run the executable that you downloaded with the name of your slack workspace (the portion before .hkn.com) and the token of your destination workspace
  - `/Users/\<name>/Downloads/slack-emoji-upload -team "hkncandidatessp21" -token "\<token>" imgs/*.*`
  - in the emoji uploader repo there is an example of uploading with a different sent of flags if there is an issue with the token method
- Open up the customize emoji page of your workspace and check that emojis are being uploaded

## User Tokens

There are 2 places where having your token is required:

1. getting the JSON of the emojis in your source workspace
2. to upload the emojis to your target

Below is how you can get the token:

1. Log into your slack workspace
2. Visit the customize section of the web app (or https://my.slack.com/customize)
3. Open your browser's developers tools, particular the web console
4. Run the following command `window.prompt('API Token', TS.boot_data.api_token)`
5. Copy the value for future use
   - make sure it has a prefix of `xoxs-...`

Thanks @jackellenberger via https://github.com/jackellenberger/emojme#finding-a-slack-token
