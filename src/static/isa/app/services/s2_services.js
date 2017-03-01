'use strict';

app.factory('RestaurantService', RestaurantService);

app.factory('RadnikService', RadnikService);

app.factory('ProviderService', ProviderService);

app.factory('TableService', TableService);

app.factory('RegionService', RegionService);

app.factory('MenuService', MenuService);

app.factory('MenuItemService', MenuItemService);

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

     function getRegions(id) {
        return $http.get('/api/restaurant/region/' + id + '/');
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


function MenuService($http) {
    var service = {};

    service.create = create;
    service.get = get;
    service.destroy = destroy;

    return service;
    
    function create(menu) {
        console.log(menu);
        return $http.post('api/restaurant/menu/create/', angular.toJson(menu));
    }

    function get(id) {
        return $http.get('api/restaurant/menu/restaurant/' + id + '/');
    }

    function destroy(id) {
        return $http.delete('api/restaurant/menu_item/' + id + '/');
    }

    function addItem(menuItem) {
        return $http.post('api/restaurant/menu_item/create/', angular.toJson(menuItem))
    }
}


function MenuItemService($http) {
     var service = {}

    service.getAll = getAll;
    service.getMenus = getMenus;

    return service;

    function getAll() {
        return $http.get('api/restaurant/menu_item/all/');
    }

     function getMenus(id) {
        return $http.get('/api/restaurant/menu/' + id + '/');
    }
}

