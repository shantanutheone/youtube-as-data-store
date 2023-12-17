# YouTube as Data Store

## Overview

This repository contains a tool that enables users to convert various types of files into a compressed zip format, convert binary content of zip to images, images to video and upload it to YouTube. Additionally, users can download the video from YouTube and revert it to the original file format.

## Sample Video

![Sample Video](https://raw.githubusercontent.com/shantanutheone/youtube-as-data-store/master/sample_video/sample.gif)


## Features

### 1. File Conversion and Compression

The tool allows users to convert different types of files to a compressed zip format, making it efficient for storage and transfer.

### 2. Video Creation

After converting to zip, the tool creates an uncompressed video from the zip file. The video is suitable for uploading to YouTube.

### 3. YouTube Integration

Users can upload the created video directly to YouTube, making it accessible to a wider audience. The repository includes instructions on how to set up the YouTube integration.

### 4. File Restoration

Anyone with access to the video can download it and use the tool to restore the original file from the video.

### 5. Password Protection

The tool supports password protection, ensuring that only authorized users can access and restore the original files.

## Usage

### Prerequisites

- Python 3.x
- Required Python packages (list dependencies here)
- YouTube API key (instructions on obtaining and setting up API key)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/youtube-as-data-store.git
   cd youtube-as-data-store


### Features

- [x] **Data Restoration**
  - [x] Use PNG format for images
  - [x] Use AVI (uncompressed) format so that youtube default compaction won't affect the content

- [ ]  **Password Protection**
  - [ ] Password protect files before conversion to zip.
  - [ ] Implement password validation during the restoration process.
  - [ ] Option to change/update the password.