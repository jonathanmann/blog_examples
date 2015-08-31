'use strict';

/* Controllers */

var appControllers = angular.module('appControllers', []);


appControllers.controller('BallotCtrl', ['$scope','$http',
  function($scope,$http) {
	console.log("got here");
	/*
    $http.get('file.php').success(function(data) {
      $scope.results = data;
    });
	*/
	$scope.tickets = [
		{
			"name": 'Ticket 1',

		},{
			"name": 'Ticket 2',

		},{
			"name": 'Ticket 3',

		},{
			"name": 'Ticket 4',
		}
	];
	
	$scope.toggleActive = function(t){

		angular.forEach($scope.tickets, function(s){
			if (s.active){
				s.active = false;
			}
		});
		t.active = !t.active;
	};
  }]);

