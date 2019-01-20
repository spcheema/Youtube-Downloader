#Simple youtube downloader made by Vaibhav Singh


import sys,subprocess

video_link,threads=sys.argv[1],sys.argv[2]

subprocess.call([

	"youtube-dl",
	"-f best ",
	video_link,
	"--external-downloader",
	"aria2c",
	"--external-downloader-args",
	"-x"+threads
	
	])


