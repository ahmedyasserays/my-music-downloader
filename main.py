from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytube import YouTube
import moviepy.editor as mp
import re
import os


# function to download the audio of the youtube video
def download(video):
    YouTube(video).streams.filter(only_audio=True).first().download(output_path="D:\music from AYS\python downloaded")




# start the driver and go to wegz channel
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/channel/UC9gXps6xggAzxjjzquNXIaQ")


# click on the videos tap
videos_tap = driver.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[2]/div')
videos_tap.click()


# scroll down and making sure you're in bottom
i = 0
while i < 100:
    scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
    i += 1

# determine if there is a new video
owned = open("owned tracks names.txt", "a+")
owned.seek(0)
owned_titles = owned.readlines()
videos_names = driver.find_elements_by_id("video-title")
new = []

for video in videos_names:
    if video.text + "\n" in owned_titles:
        continue
    else:
        new.append(video)


# loop over the new videos, download them and create the mp4 list
for song in new:
    link = song.get_attribute('href')
    download(link)
    owned.write(song.text + "\n")



owned.close()

# convert the mp4 files to mp3
tgt_folder = 'D:\music from AYS\python downloaded'
for file in [n for n in os.listdir(tgt_folder) if re.search('mp4', n)]:
    full_path = os.path.join(tgt_folder, file)
    output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path).subclip(10, )  # disable if do not want any clipping
    clip.write_audiofile(output_path)

driver.close()

