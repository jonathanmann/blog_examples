'use strict';

/* App Module */
var app = angular.module('app', [
  'ngRoute',
  'appControllers',
  'ui.bootstrap'
]);

app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
	  when('/ballot', {
        templateUrl: 'views/ballot.html',
        controller: 'BallotCtrl'
      }).
	  when('/receipt/:ticket', {
        templateUrl: 'views/receipt.html',
        controller: 'ReceiptCtrl'
      }).
		when('/result', {
        templateUrl: 'views/result.html',
        controller: 'ResultCtrl'
      }).
      otherwise({
        redirectTo: '/ballot' 
      });
  }]);
