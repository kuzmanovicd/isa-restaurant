'use strict';

app.factory('RestaurantService', RestaurantService);


app.factory('RestaurantManagerService', RestaurantManagerService);



function RestaurantService($http) {
    var service = {};
    
    service.create = create;
    service.update = update;
    service.get = get;
    service.selectedProdavnica = {};
    
    return service;
    
    function create(prodavnica) {
        return $http.post('api/prodavnica/add', angular.toJson(prodavnica));
    }
    
    function get(id) {
        return $http.get('/api/restaurant/restaurant/' + id + '/');
    }
    
    function update(prodavnica) {
        return $http.put('api/prodavnica/update', angular.toJson(prodavnica));
    }
}


/*
function RestaurantManagerService($http) {
    var service = {};

    service.Create = Create;
    service.Update = Update;
    service.Delete = Delete;
}

*/