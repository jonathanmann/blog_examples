'use strict';

/* Controllers */

var appControllers = angular.module('appControllers', []);

appControllers.controller('BallotCtrl', ['$scope','$http',
        function($scope,$http) {

            $http.get('api/tickets').success(function(data) {
                $scope.tickets = data;
            });


            $scope.submit_form = function(){
                $http({
                    method  : 'POST',
                    url     : 'api/tickets/',
                    data    : $.param($scope.vote_data), 
                    headers : { 'Content-Type': 'application/x-www-form-urlencoded' } 
                })
                .success(function(data) {
                    if (!data.success) {
                        // if not successful, bind errors to error variables
                        console.log('error');
                        console.log(data);
                    } else {
                        // if successful, bind success message to message
                        $scope.message = data.message;
                        //console.log($scope.message);
                        window.location = '#/receipt/' + $scope.message;
                    }
                });
            };

            $scope.toggleActive = function(t){

                angular.forEach($scope.tickets, function(s){
                    if (s.active){
                        s.active = false;
                    }
                });
                t.active = !t.active;
                $scope.selected_id = t.id;
                $scope.vote_data = {"dct" : '{"table" : "ballot","ticket_id" : "' + $scope.selected_id + '","ticket_name" :"'+ t.name + '"}'};
            };
        }]);

appControllers.controller('ReceiptCtrl', ['$scope','$http','$routeParams',
        function($scope,$http,$routeParams) {
            $scope.uuid = $routeParams.uuid;
            $http.get('api/tickets/' + $scope.uuid).success(function(data) {
                $scope.ticket = data[0];
            });
        }]);
