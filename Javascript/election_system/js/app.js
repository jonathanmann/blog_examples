'use strict';

/* App Module */

var app = angular.module('app', [
  'ngRoute',
  'appControllers'
]);

app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
	  when('/ballot', {
        templateUrl: 'views/ballot.html',
        controller: 'BallotCtrl'
      }).
      otherwise({
        redirectTo: '/ballot' 
      });
  }]);
