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
                ditch_empty: false,
                ditch_alarm: false,
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
            $scope.ditch = {
                level: "empty",
                alarm: 'Okay'
            };

            $scope.states = {
                'north' : { label: 'North On', call: false },
                'south' : { label: 'South On', call: false },
                'pump'  : { label: 'Pump On', call: false }
            };

            function onStatus(status) {
                $scope.info = status;
                var d = $scope.ditch;
                var i = $scope.info;

                d.alaram ='okay';
                if (i.ditch_empty) {
                    d.level = 'empty';
                } else if (i.ditch_alaram) {
                    d.alaram ='ALARMED';
                    d.level = 'FULL';
                } else {
                    d.level = i.ditch_inches;
                }

                _.each(['north','south','pump'], function(zone) {
                    var call = status[zone+"_call"];
                    var zoneName = zone.charAt(0).toUpperCase() + zone.slice(1);
                    console.log("Zone Name:" + zoneName);

                    $scope.states[zone].call = call;
                    $scope.states[zone].label = zoneName + (call ? " Off" : " On");
                    console.log('Status for ' + zone + " " + call);
                });

            }

            $http.get('/api/v1/status/').success(function (data) {
                onStatus(data);
            });

            $interval(function () {
                $http.get('/api/v1/status/').success(function (data) {
                    onStatus(data);
                });
            }, DitchParams.statusPollRate);


            var history_token = null;
            var chart_data = {
                'timestamp': [],
                'ditch': [],
                'sump': []
            };

            var chart = new Highcharts.Chart({
                chart: {
                    renderTo: 'ditch_level',
                    type: 'line'
                },
                title: {
                    text: 'Ditch Levels'
                },
                xAxis: {
                    time: chart_data.timestamps,
                },
                yAxis: {
                    title: {
                        text: 'Ditch Level (in)'
                    }
                },
                series: [{
                    name: 'Ditch Level',
                    data: chart_data.ditch
                }, {
                    name: 'Sump Levels',
                    data: chart_data.sump
                }]
            });

            function onHistory(data) {
                //history_token = data.token;

                var ts = [];
                var dl = [];
                var sl = [];

                _.each(data, function(item) {
                    ts.push(item[0]);
                    dl.push(item[1]);
                    sl.push(item[2]);
                });

                //chart.xAxis.addPoint(ts[0]);
                chart.series[0].addPoint([ts[0], dl[0]]);
                chart.series[1].addPoint([ts[0], sl[0]]);

            }

            $http.get('/api/v1/history/').success(function (data) {
                onHistory(data);
            });


            $interval(function () {
                $http.get('/api/v1/history/').success(function (data) {
                    onHistory(data);
                });
            }, DitchParams.statusPollRate);


            console.log("Polling every " + DitchParams.statusPollRate + " milliseconds.");

            $scope.toggleState = function(zone) {
                if ($scope.states[zone].call) {
                    $http.post('/api/v1/' + zone + '/off/').success(function () {});
                } else {
                    $http.post('/api/v1/' + zone + '/on/').success(function () {});
                }
            }

        }
    ]
);

