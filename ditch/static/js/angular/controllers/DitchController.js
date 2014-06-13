/**
 * Copyright: Aspen Labs, LLC. 2011
 * User: kutenai
 * Date: 6/14/13
 * Time: 6:51 PM
 */

app.controller('DitchController',
    ['$scope','$http',
        function($scope, $http) {
        $scope.info = {
            ditch_inches    : 12.3,
            sump_inches     : 19.1,
            pump_on         : false,
            north_on        : false,
            south_on        : false
        };

        $http.get('/api/v1/gardeners/').success(function(data) {
            $scope.gardeners = data;
        });
    }]
);

