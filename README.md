# lambda-gtfsrt

[![License](https://img.shields.io/dub/l/vibe-d.svg)](http://doge.mit-license.org)

Parse vehicle positions and trip updates from a GTFS-realtime feed using AWS Lambda. Particularly useful when hooked up as a JSON API using AWS's [API Gateway](https://aws.amazon.com/api-gateway/).

# Usage

The Lambda handler expects a URL to passed through the event using the key `url` (i.e. `event['url']`).

# Quickstart

1. Build this project into a zip file by running `build.sh`.
2. Create a Lambda function through the AWS console or the [AWS CLI](http://docs.aws.amazon.com/cli/latest/reference/lambda/index.html) using the built zip file.
3. [OPTIONAL] Create an API Gateway endpoint that calls the Lambda function you created in step 2. To allow users of this endpoint to pass an arbitrary URL to the Lambda function, setup an [input mapping template](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#input-variable-reference) in API Gateway.
