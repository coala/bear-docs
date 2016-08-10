'use strict';

angular.module('coalabearDocsApp')
    .controller('BearsCtrl', ["$scope", "$window", "$rootScope", "$http", "$routeParams",
        function($scope, $window, $rootScope, $http, $filterByFilter, $fuzzyFilter,
            $routeParams)
        {
            var parseCoalaProject = function()
            {
                $scope.languages = [];
                $scope.bearslist = $rootScope.bears;
                $scope.bearsTotal = $scope.bearslist.length;
                for (var languages in $rootScope.bears)
                {
                    for (var lang in $rootScope.bears[languages].LANGUAGES)
                    {
                        if (!$scope.languages.includes($rootScope.bears[languages].LANGUAGES[lang]))
                        {
                            $scope.languages.push($rootScope.bears[languages].LANGUAGES[lang]);
                        }
                    }
                }
                $scope.languages.sort(function(a, b)
                {
                    return a.toLowerCase().localeCompare(b.toLowerCase());
                });
                $scope.reset = function()
                {
                    $scope.bearslist = $rootScope.bears;
                    $scope.message = ''
                    $scope.bearsTotal = $scope.bearslist.length;
                    return $scope.bearslist;
                }
                $scope.alllanguages = [];
                for (var languages in $rootScope.bears)
                {
                    for (var lang in $rootScope.bears[languages].LANGUAGES)
                    {
                        $scope.alllanguages.push($rootScope.bears[languages].LANGUAGES[lang]);
                    }
                }
                $scope.alllanguages.sort(function(a, b)
                {
                    return a.toLowerCase().localeCompare(b.toLowerCase());
                });
                $scope.counts = {};
                for (var i = 0; i < $scope.alllanguages.length; i++)
                    $scope.counts[$scope.alllanguages[i]] = ($scope.counts[$scope.alllanguages[i]] + 1) || 1;
                console.log($scope.counts);

                $scope.filterFunction = function(option)
                {
                    $scope.bearslist = [];
                    $scope.message = option;
                    for (var languages in $rootScope.bears)
                    {
                        for (var lang in $rootScope.bears[languages].LANGUAGES)
                        {
                            if (option == $rootScope.bears[languages].LANGUAGES[lang])
                            {
                                $scope.bearslist.push($rootScope.bears[languages]);
                            }
                        }
                    }
                    $scope.bearsTotal = $scope.bearslist.length;
                    return $scope.bearslist;
                };
                $scope.scrollToTop = function()
                {
                    $window.scrollTo(0, 0);
                }
                $scope.isActive = false;
            };
            parseCoalaProject();
        }
    ]);
