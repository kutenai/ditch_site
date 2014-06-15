/**
 * Copyright: Aspen Labs, LLC. 2011
 * User: kutenai
 * Date: 6/14/13
 * Time: 6:51 PM
 */

app.controller('DitchController',
    ['$scope','$http','$interval',
        function($scope, $http,$interval) {
            $scope.info = {
                ditch_inches: 12.3,
                sump_inches:  19.1,
                pump_on:      false,
                north_on:     false,
                south_on:     false,
                pump_call:    false,
                north_call:   false,
                south_call:   false,
                ditch_reading: 0.0,
                sump_reading: 0.0
            };
            $scope.northButton = "North On";
            $scope.southButton = "South On";
            $scope.pumpButton = "Pump On";

            function onStatus(status) {
                $scope.info = status;

                if (status.north_call) {
                    $scope.northButton = "North Off";
                } else {
                    $scope.northButton = "North On";
                }
            };

            $http.get('/api/v1/status/').success(function (data) {
                onStatus(data);
            });

            $interval(function () {
                $http.get('/api/v1/status/').success(function (data) {
                    onStatus(data);
                });
            }, DitchParams.statusPollRate);

            $scope.northToggle = function () {
                if ($scope.info.north_call) {
                    $http.post('/api/v1/north/off/').success(function () {});
                } else {
                    $http.post('/api/v1/north/on/').success(function () {});
                }
            };

            $scope.southToggle = function () {
                if ($scope.info.south_call) {
                    $http.post('/api/v1/south/off/').success(function () {});
                } else {
                    $http.post('/api/v1/south/on/').success(function () {});
                }
            };

            $scope.pumpToggle = function () {
                if ($scope.info.pump_call) {
                    $http.post('/api/v1/pump/off/').success(function () {});
                } else {
                    $http.post('/api/v1/pump/on/').success(function () {});
                }
            };
        }
    ]
);

