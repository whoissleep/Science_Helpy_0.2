#!/bin/bash

curl --request GET --user "$1:$2" \
--aws-sigv4 "aws:amz:ru-central1:s3" \
--output "$5" \
"https://storage.yandexcloud.net/$3/$4"\
--verbose


