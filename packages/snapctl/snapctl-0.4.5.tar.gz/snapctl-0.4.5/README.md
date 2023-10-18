# Snapser CLI Tool

## Dependencies
The Snapser CLI tool depends on Python 3.X and Pip. MacOS comes pre isntalled with Python. But
please make sure you are running Python 3.X. On Windows, you can download Python 3.X from the
Windows store. Some of the commands also need `docker`.

## Installation
Installing PIP on MacOS
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

Installing PIP on Windows
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Once you have Python and Pip installed
```bash
pip install --user snapctl
```
If you also have Python 2.X on your machine, you may have to run instead
```bash
pip3 install --user snapctl
```

**Important** Please verify that your python path has been added to $PATH

## Upgrade
Upgrade your snapctl version
```bash
pip install --user snapctl --upgrade
```

## Setup
### Get your Snapser Access Key
Log in to your Snapser account. Click on your user icon on the top right and select, User Settings.
Under developer key tab you will be able to copy your Access Key.

### Setup a local config
Create a file named `~/.snapser/config`. Open it using the editor of your choice and replace <key> with your
personal Snapser Access key. Save the file.
```text
[default]
snapser_access_key = <key>
```

Or you can run the following command

on MacOSX
```bash {{title: 'MacOSX'}}
# $your_api_key = Your Snapser developer key
echo -e "[default]\nSNAPSER_API_KEY=$your_api_key" > ~/.snapser/config
```
on Windows Powershell
```bash {{title: 'Windows Powershell'}}
# $your_api_key = Your Snapser developer key
echo "[default]
SNAPSER_API_KEY=$your_api_key" | Out-File -encoding utf8 ~\.snapser\config
```


## Verify Snapctl installation
```bash
snapctl --version
```
You should see the latest snapctl version in the output


## Supported commands
Run the following to see the list of commands Snapser supports
```bash
snapctl --help
```

## Advanced Setup
Snapser by default supports access to multiple accounts. You can create multiple profiles in your Snapser config
`~/.snapser/config`.
```text
[profile personal]
snapser_access_key = <key>

[profile professional]
snapser_access_key = <key>

```
You can then set an environment variable telling Snapser which profile you want to use.
```bash
# Mac
export SNAPSER_PROFILE="my_profile_name";

```
```bash
# Windows
setx SNAPSER_PROFILE="my_profile_name";

```
Or you can pass `--profile my_profile_name` with every command to tell Snapser to use a particular profile.


## Commands

### BYO Snap - Bring your own Snap
#### 1. byosnap help
See all the supported commands
```bash {{ title: 'Bring your own Snap - Help' }}
# Help for the byosnap command
snapctl byosnap --help
```

#### 2. byosnap create
Ability to create a custom snap.
```bash {{ title: 'Bring your own Snap - Create' }}
# Help for the byosnap command
snapctl byosnap create --help

# Create a new snap
# $byosnap_sid = Snap ID for your snap. Start start with `byosnap-`
# $name = User friendly name for your BYOSnap
# $desc = User friendly description
# $platform = One of linux/arm64, linux/amd64
# $language = One of go, python, ruby, c#, c++, rust, java, node

# Example:
# snapctl byosnap create byosnap-jinks-flask --name "Jinks Flask Microservice" --desc "Custom Microservice" --platform "linux/arm64" --language "go"
snapctl byosnap create $byosnap_sid --name "$name" --desc "$desc" --platform "$platform" --language "$language"
```

#### 3. byosnap publish-image
Ability to publish a custom snap code image.
```bash {{ title: 'Bring your own Snap - Publish a new image' }}
# Help for the byosnap command
snapctl byosnap publish-image --help

# Publish a new image
# $byosnap_sid = Snap ID for your snap
# $image_tag = An image tag for your snap
# $code_root_path = Local code path where your Dockerfile is present
# Example:
# snapctl byosnap publish-image byosnap-jinks-flask --tag my-first-image --path /Users/DevName/Development/SnapserEngine/jinks_flask
snapctl byosnap publish-image $byosnap_sid --tag $image_tag --path $code_root_path
```

#### 4. byosnap publish-version
Ability to publish a new version for your Snap.
```bash {{ title: 'Bring your own Snap - Publish a new version' }}
# Help for the byosnap command
snapctl byosnap publish-version --help

# Publish a new image
# $byosnap_sid = Snap ID for your snap
# $image_tag = An image tag for your snap
# $prefix = Prefix for your snap Eg: /v1
# $version = Semantic version for your snap Eg: v0.0.1
# $ingress_port = Ingress port for your snap Eg: 5003
# Example:
# snapctl byosnap publish-image byosnap-jinks-flask --tag my-first-image --prefix /v1 --version v0.0.1 --http-port 5003
snapctl byosnap publish-version $byosnap_sid --tag $image_tag --prefix $prefix --version $version --http-port $ingress_port
```

#### 5. byosnap upload-docs
Ability to upload swagger.json and README.md for you Snap
```bash {{ title: 'Bring your own Game Server - Publish a new image' }}
# Help for the byogs command
snapctl byosnap upload-docs --help

# Publish a new image
# $byogs_sid = Game server ID for your snap
# $image_tag = An image tag for your snap
# $code_root_path = Local code path where your swagger.json and README.md files are present
# Example:
# snapctl byosnap upload-docs byosnap-jinks-flask --tag my-first-image --path /Users/DevName/Development/SnapserEngine/jinks_flask
snapctl byosnap upload-docs $byogs_sid --tag $image_tag --path $code_root_path
```

### BYO Game Server - Bring your own Game Server
#### 1. byogs help
See all the supported commands
```bash {{ title: 'Bring your own Game Server - Help' }}
# Help for the byogs command
snapctl byogs --help
```

#### 2. byogs create
Ability to create a custom game server.
```bash {{ title: 'Bring your own Game Server - Create' }}
# Help for the byosnap command
snapctl byogs create --help

# Create a new snap
# $byogs_sid = Game server ID for your snap. Should start with `byogs-`
# $name = User friendly name for your BYOGs
# $desc = User friendly description
# $platform = Currently only supported platform is linux/amd64
# $language = One of go, python, ruby, c#, c++, rust, java, node

# Example:
# snapctl byogs create byosnap-jinks-gs --name "Jinks Flask Microservice" --desc "Custom Microservice" --platform "linux/arm64" --language "go"
snapctl byogs create $byogs_sid --name "$name" --desc "$desc" --platform "$platform" --language "$language"
```

#### 3. byogs publish-image
Ability to publish your custom game server image.
```bash {{ title: 'Bring your own Game Server - Publish a new image' }}
# Help for the byogs command
snapctl byogs publish-image --help

# Publish a new image
# $byogs_sid = Game server ID for your snap
# $image_tag = An image tag for your snap
# $code_root_path = Local code path where your Dockerfile is present
# Example:
# snapctl byogs publish-image byosnap-jinks-gs --tag my-first-image --path /Users/DevName/Development/SnapserEngine/jinks_flask
snapctl byogs publish-image $byogs_sid --tag $image_tag --path $code_root_path
```

#### 4. byogs publish-version
Ability to publish a new version for your Game server.
```bash {{ title: 'Bring your own Snap - Publish a new version' }}
# Help for the byogs command
snapctl byogs publish-version --help

# Publish a new image
# $byogs_sid = Snap ID for your snap
# $image_tag = Any image tag for your snap
# $prefix = Prefix for your snap Eg: /v1
# $version = Semantic version for your snap Eg: v0.0.1
# $ingress_port = Ingress port for your snap Eg: 5003
# Example:
# snapctl byogs publish-image byosnap-jinks-gs --tag my-first-image --prefix /v1 --version v0.0.1 --http-port 5003
snapctl byogs publish-version $byogs_sid --tag $image_tag --prefix $prefix --version $version --http-port $ingress_port
```

### Snapend
#### 1. snapend help
See all the supported commands
```bash {{ title: 'Snapend - Help' }}
# Help for the byogs command
snapctl snapend --help
```

#### 2. Snapend Downloads
Download SDKs and Protos for your Snapend
```bash {{ title: 'Snapend - Downloads' }}
# Help for the byogs command
snapctl snapend download --help

# Download your Snapend SDK and Protos
# $snapend_id = Cluster Id
# $category = client-sdk, server-sdk, protos
# $sdk_type = One of the supported SDK names:
# client-sdk(unity, unreal, roblox, godot, cocos, ios-objc, ios-swift, android-java, android-kotlin, web-ts, web-js),
# server-sdk(csharp, cpp, lua, ts, go, python, kotlin, java, c, node, js, perl, php, closure, ruby, rust),
# protos(go)
# Example:
# snapctl snapend download gx5x6bc0 --category client-sdk --type unity
snapctl snapend download $snapend_id --category $category --type $sdk_type
```

#### 3. Update Snapend BYOSnap or BYOGs versions
Update your BYOSnap or BYOGs versions for the Snapend
```bash {{ title: 'Snapend - Update BYOSnap or BYOGs' }}
# Help for the byogs command
snapctl snapend update --help

# Update your Snapend with new BYOSnaps and BYOGs
# $snapend_id = Cluster Id
# $byosnaps = Comma separated list of BYOSnap ids and version.
# $byogs = Comma separated list of BYOGs fleet name, id and version.
# --blocking = (Optional) This makes sure the CLI waits till your Snapend is live.
# Note atleast one of the two needs to be present
# Example:
# snapctl snapend update gx5x6bc0 --byosnaps byosnap-service-1:v1.0.0,byosnap-service--2:v1.0.0 --byogs byogs-fleet-one:gs-1:v0.0.1,my-fleet-two:gs-2:v0.0.4
# snapctl snapend update gx5x6bc0 --byosnaps byosnap-service-1:v1.0.0,byosnap-service--2:v1.0.0 --byogs byogs-fleet-one:gs-1:v0.0.1,my-fleet-two:gs-2:v0.0.4 --blocking
snapctl snapend update $snapend_id --byosnaps $byosnaps --byogs $byogs --blocking
```

#### 4. Get the Snapend state
Get the Snapend state
```bash {{ title: 'Snapend - Get state' }}
# Help for the byogs command
snapctl snapend state --help

# Get the Snapend state
# $snapend_id = Cluster Id
# Example:
# snapctl snapend state gx5x6bc0
snapctl snapend state $snapend_id
```

