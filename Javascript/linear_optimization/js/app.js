linear_demo = angular.module('linear_optimization_demo', ['n3-line-chart']);
linear_demo.controller('OptimizationCtrl',['$scope','$http',
		function($scope,$http) {
			$http.get('data/plot_data.json').success(function(data) {
				$scope.data= data;
			});
			$http.get('data/series.json').success(function(data) {
				$scope.options = { lineMode: "linear", 
					/*
					axes: {
						x: {key: 'x', ticksFormat: '.2f', type: 'linear', min: 0, max: 250, ticks: 2}
					},*/
					series: data
				};
			});
		}]);	
