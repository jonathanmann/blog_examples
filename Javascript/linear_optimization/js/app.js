linear_demo = angular.module('linear_optimization_demo', ['n3-line-chart']);
linear_demo.controller('OptimizationCtrl',['$scope','$http',
		function($scope,$http) {
			$http.get('data/plot_data.json').success(function(data) {
				$scope.data= data;
			});
			$http.get('data/series.json').success(function(data) {
				$scope.options = {lineMode: "cardinal", 
					series: data
				};
			});
		}]);	
