# Load Testing for API

[Locust](https://locust.io/)to load test the API.

## :point_right: Testing against localhost

Set up the .load_env.example file with proper environment data

To run setup the load tests run the setup.sh file, incase setup file has insufficient privilege use `chmod +x` to give execute permissions.

`./setup.sh`

Alternatively, run the command in setup.sh individually in bash.

To run the tests in local go to folder load_test and execute below command:

`locust`

 Open the locust dashboard at http://127.0.0.1:8089/

 Choose the number of users & spawn rate, then run the tests.

## :point_right: Testing against staging

## :point_right: Dependencies

## :point_right: Post-testing cleanup

