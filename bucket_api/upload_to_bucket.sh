#!/bin/bash

curl --request PUT --user "$1:$2" \
--aws-sigv4 "aws:amz:ru-central1:s3" \
--upload-file "$4" \
--verbose "https://storage.yandexcloud.net/$3/"
