# Instagram Downloader

This Program simply download Profile of Public Account like Pictures(inc. Display Picture), Videos, Captions and Hashtags
## Resource
````python
pip install instaloader
````

## CommandLine

1. Anonymously Downloading  
````cmd
instaloader profile {profile_name} -V --no-captions --no-metadata-json --no-compress-json
````

2. Download Private Profiles
````cmd
instaloader --login {username} profile {profile_name} -V --no-captions --no-metadata-json --no-compress-json  
````
**or**
````cmd
instaloader --login {username} {profile_name} -V --no-captions --no-metadata-json --no-compress-json  
````
