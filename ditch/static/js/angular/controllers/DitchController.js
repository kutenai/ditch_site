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
            ditch_inches    : 12.3,
            sump_inches     : 19.1,
            pump_on         : false,
            north_on        : false,
            south_on        : false
        };

        $http.get('/api/v1/status/').success(function(data) {
            $scope.info = data;
        });

        $interval(function() {
            $http.get('/api/v1/status/').success(function(data) {
                $scope.info = data;
            });
        }, DitchParams.statusPollRate);
    }]
);

