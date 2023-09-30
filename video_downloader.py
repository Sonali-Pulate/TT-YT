from TikTokApi import TikTokApi
import urllib.request
import os
import subprocess

# Get the list of video file names in the `videos` folder.
def getlist():
    video_file_names = subprocess.check_output(["ls", "videos"]).decode()

    oldfile=set(video_file_names.split("\n"))
    oldfile.remove('')

    newfile=set(video_file_names.replace(" ", "_").split("\n"))
    newfile.remove('')
    
    for i in range(len(newfile)):
        os.rename("videos/"+list(set(list(oldfile)))[i], "videos/"+list(set(list(newfile)))[i])

    return newfile

def downloader(isDownloaded):
    if isDownloaded:
        print("Downloaded video!")
        print("Testing...")
        return getlist()
        
    api = TikTokApi.get_instance()
    trending = api.by_trending(count=1, custom_verifyFp="verify_ln45vr44_CPyuBPXn_fvs1_4w95_9e4A_dAjl4qWiGhxX")
    for tiktok in trending:
        tvideo = tiktok['video']
        link = tvideo['downloadAddr']
        author = tiktok['author']
        username = author['uniqueId']
        id = tiktok['id']
        desc = tiktok['desc']
        print("Downloading video...")
        urllib.request.urlretrieve(link, f'{username}-{id}.mp4')
    if len(desc) > 75:
        desc = desc[:75]
    title = f"{desc} - @{username} - For You"
    description = f"Credit to the original creator, @{username}. Check out their other content here: https://tiktok.com/@{username} #shorts"
    print("Downloaded video!")
    print(title)
    return dict(
        title=title,
        description=description,
        file=f'{username}-{id}.mp4'
    )