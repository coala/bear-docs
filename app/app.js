'use strict';

angular
  .module('coalabearDocsApp', ['ngRoute','angular.filter'])
  .run(['$rootScope', '$http', function($rootScope, $http) {
    $http.get("data/bears.json")
      .then(function(coala_bears) {
        $rootScope.bears = coala_bears.data.bears;
    });
  }])
  .config(['$routeProvider',function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'app/views/bears.html',
        controller: 'BearsCtrl',
        controllerAs: 'bears'
      })
      .when('/:bearName', {
        templateUrl: 'app/views/detail.html',
        controller: 'DetailCtrl',
        controllerAs: 'details'
      })
      .when('/lang/:language', {
        templateUrl: 'app/views/language.html',
        controller: 'LangCtrl',
        controllerAs: 'language'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);
