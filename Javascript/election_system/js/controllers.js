'use strict';

/* Controllers */

var appControllers = angular.module('appControllers', []);

appControllers.controller('BallotCtrl', ['$scope','$http',
		function($scope,$http) {

			$http.get('api/tickets').success(function(data) {
				$scope.tickets = data;
			});

			$scope.vote_data = [{"vote" : "1","description" :"test party"}];

			$scope.submit_form = function(){
                $http({
                    method  : 'POST',
                    url     : 'api/tickets/11',
                    data    : $.param($scope.vote_data), 
                    headers : { 'Content-Type': 'application/x-www-form-urlencoded' } 
                })
                .success(function(data) {
                    console.log('data');
                    console.log(data);

                    if (!data.success) {
                        // if not successful, bind errors to error variables
                        console.log('error');
												console.log(data);
                    } else {
                        // if successful, bind success message to message
												console.log('happened');
                        $scope.message = data.message;
                        console.log($scope.message);
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
			};
		}]);

