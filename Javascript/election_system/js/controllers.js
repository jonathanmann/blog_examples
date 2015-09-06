'use strict';

/* Controllers */

var appControllers = angular.module('appControllers', []);

appControllers.controller('BallotCtrl', ['$scope','$http',
  function($scope,$http) {
	
    $http.get('api/tickets').success(function(data) {
      $scope.tickets = data;
    });

	$scope.toggleActive = function(t){

		angular.forEach($scope.tickets, function(s){
			if (s.active){
				s.active = false;
			}
		});
		t.active = !t.active;
	};
  }]);

