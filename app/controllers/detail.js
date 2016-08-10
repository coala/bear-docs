'use strict';

angular.module('coalabearDocsApp')
    .controller('DetailCtrl', ["$scope", "$rootScope", "$http", '$routeParams',
        function($scope, $rootScope, $http, $routeParams) {
            var parseCoalaProject = function() {
                for (var bear in $rootScope.bears) {
                    if ($rootScope.bears[bear].name == $routeParams.bearName) {
                        $scope.requiredBear = $rootScope.bears[bear];
                    }

                }
            };
            parseCoalaProject();
        }
    ]);
