'use strict';

angular.module('coalabearDocsApp')
    .controller('LangCtrl', ["$scope", "$rootScope", "$http", '$routeParams',
        function($scope, $rootScope, $http, $routeParams) {
            var parseCoalaProject = function() {
                $scope.bearslist = [];
                for (var languages in $rootScope.bears) {
                    for (var lang in $rootScope.bears[languages].LANGUAGES) {
                        console.log($rootScope.bears[languages].LANGUAGES[lang]);
                        if ($rootScope.bears[languages].LANGUAGES[lang] == unescape($routeParams.language)) {
                            $scope.bearslist.push($rootScope.bears[languages]);
                            $scope.bearsTotal = $scope.bearslist.length;

                        }
                    }
                }
                return $scope.bearslist;
            };
            parseCoalaProject();
        }
    ]);
