#!/bin/bash
rm -rf oeml_data.zip
rm -rf ./data
gdown https://drive.google.com/uc?id=1GqA4lKvMT7GpX9MclpyV0IdqZBZAX88w --output oeml_data.zip
unzip oeml_data.zip -d .
rm -rf oeml_data.zip