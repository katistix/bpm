bpm is a minimalist code package manager. You can think of it like a tool to download small (and usually not production ready) projects or scripts while also offering a more standardized way of managing and running them.


## It can run anything!

By design, bpm **does not** include any compilers, libraries, modules, packages or other tools necessary for running the [boxes](#what-is-a-box). But by installing a box, bpm can install it's required dependencies too, for more information [Learn more about boxinstall files](#learn-about-boxinstall).

## What is a box?
A box is, simply put, just a named folder, it contains a [box_config.json](#learn-about-box_configjson) file and a [boxfiles](#learn-about-boxfiles) file. Some boxes may also contain a [boxinstall](#learn-about-boxinstall) file. Besides that, a box contains all the files you usually have in a project.

## Learn about *box_config.json*
This is a required file! It tells your bpm installation usefull information like the *installed version*, *short description* acout the box, and also *how to run the box*.

This is the structure of a *box_config.json* file
```json
{
	"version": "0.0.1",
	"description": "This is my box :)",
	"run": "node index.js"
}
```

## Learn about *boxfiles*
This is a required file! It tells your bpm installation what files to download from the *remote bpm box repository*.

This is the structure of a *boxfiles* file
```
# This is a comment, it is ignored
index.js
box_config.json
```
***NOTE!*** **Do not forget to include `box_config.json` in your *boxfiles* file**

## Learn about *boxinstall*
This is an optional file! It tells your bpm installation what commands to run while installing a box (after downloading the files from *boxfiles*)

This is the structure of a *boxinstall* file
```
# This is a comment, it is ignored
echo Hello
npm install
```
