'use strict';

app.factory('RestaurantService', RestaurantService);

app.factory('RadnikService', RadnikService);

app.factory('ProviderService', ProviderService);

app.factory('TableService', TableService);

app.factory('RegionService', RegionService);

function RestaurantService($http) {
    var service = {};
    
    service.create = create;
    service.update = update;
    service.get = get;
    service.getAll = getAll;
    service.selectedProdavnica = {};
    
    return service;
    
    function getAll() {
        return $http.get('api/restaurant/restaurant/all/');
    }

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


// service za Employee (Radnika)
function RadnikService($http) {
    var service = {};

    service.create = create;

    return service;
    
    function create(link, employee) {
        console.log(employee);
        return $http.post('api/users/' + link + '/create/', angular.toJson(employee));
    }

     
}

//service za Providera
function ProviderService($http) {
    var service = {};

    service.create = create;

    return service;
    
    function create(provider) {
        console.log(provider);
        return $http.post('api/users/provider/create/', angular.toJson(provider));
    }

}


//service za Table
function TableService($http) {
    var service = {}

    service.getAll = getAll;
    service.getRegions = getRegions;

    return service;

    function getAll() {
        return $http.get('api/restaurant/table/all/');
    }

     function getRegions() {
        return $http.get('/api/restaurant/region/all/');
    }

}

//service za region
function RegionService($http) {
    var service = {};

    service.create = create;

    return service;
    
    function create(region) {
        console.log(region);
        return $http.post('api/restaurant/region/create/', angular.toJson(region));
    }
}

