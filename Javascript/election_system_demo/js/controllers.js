'use strict';

/* Controllers */

var appControllers = angular.module('appControllers', []);

appControllers.controller('BallotCtrl', ['$scope','$http',
		function($scope,$http) {
			$http.get('data/tickets.json').success(function(data) {
				$scope.tickets = data;
				});
			$scope.submit_form = function(){
				window.location = '#/receipt/' + $scope.selected_ticket;
			};

			$scope.toggleActive = function(t){

				angular.forEach($scope.tickets, function(s){
					if (s.active){
						s.active = false;
					}
				});
				t.active = !t.active;
				$scope.selected_id = t.id;
				$scope.selected_ticket = t.name;
			};
		}]);

appControllers.controller('ReceiptCtrl', ['$scope','$http','$routeParams',
		function($scope,$http,$routeParams) {

			// generate uuid
			var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
				var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
				return v.toString(16);
			});

			$scope.uuid = uuid; 
			$scope.ticket = $routeParams.ticket;

			//replace uuid for demonstartion purposes
			if ($scope.ticket == "Socialist"){
				$scope.uuid = "01ee7361-9174-4399-bfc1-880ab2a66e7e";
			} else if ($scope.ticket == "Neutral"){
				$scope.uuid = "02878eef-421f-4c36-86b0-660a5179ffd6";
			} else if ($scope.ticket == "Libertarian"){
				$scope.uuid = "03a771ed-c3e4-4010-a62e-dea04bb84009";
			} else if ($scope.ticket == "Third"){
				$scope.uuid = "08fed833-eaff-4436-9d44-bdfc0632ddb4";
			} else {
				$scope.uuid = "invalid";
			}

		}]);

appControllers.controller('ResultCtrl', ['$scope','$http',
		function($scope,$http) {
			 $http.get('data/votes.json').success(function(data) {
				$scope.votes = data;
				});
			 $http.get('data/summary.json').success(function(data) {
				$scope.results = data;
				});

		}]);

