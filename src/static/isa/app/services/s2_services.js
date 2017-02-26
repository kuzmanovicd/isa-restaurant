'use strict';

app.factory('RestaurantService', RestaurantService);

app.factory('RadnikService', RadnikService);

app.factory('ProviderService', ProviderService);

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
    
    function create(link, provider) {
        console.log(provider);
        return $http.post('api/users/' + link + '/create/', angular.toJson(provider));
    }

}

