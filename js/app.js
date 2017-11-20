var app = angular.module('rateLevels', []);

//create a model of items for rating
app.controller('itemListController', function itemListController($scope) {
  $scope.items = [
    {
      name: 'Stress level',
      level: 0
    }, {
      name: 'Anxiety level',
      snippet: 0
    }
  ];
});