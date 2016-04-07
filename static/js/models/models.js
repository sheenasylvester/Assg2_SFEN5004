(function (document, window, $, Backbone, _){

	window.UTT = {
		Routers			: {},
		Views 			: {},
		Models			: {},
		Collections		: {},
		templateLoader 	: {}
	};

	UTT.Models.RestaurantModel = Backbone.Model.extend({		

		urlRoot : '/restaurants',

		initialize: function(){	
			console.log('sending data to:' + this.urlRoot);		
		},

		defaults: {			
			"id": null, 
			"restaurant_address": null, 
			"restaurant_image": null,
			"restaurant_name": null
	    }
	});

	UTT.Collections.RestaurantCollection = Backbone.Collection.extend({
		model 	: UTT.Models.RestaurantModel,
		url 	: '/restaurants'
	});


	//User Model and Collection
	UTT.Models.MeetAndEatUser = Backbone.Model.extend({		//Extends on Backbone Model to create Custom Model

		urlRoot : '/userlist',

		initialize: function(){	
			console.log('sending data to:' + this.urlRoot);		
		},

		defaults: {			
			"id": null, 
			"password_hash": null, 
			"email": null
	    }
	});

	UTT.Collections.UserCollection = Backbone.Collection.extend({
		model 	: UTT.Models.MeetAndEatUser,
		url 	: '/userlist'
	});

	
	//Request Model and Collection
	UTT.Models.MeetAndEatRequest = Backbone.Model.extend({		//Extends on Backbone Model to create Custom Model

		urlRoot : '/meetrequests',

		initialize: function(){	
			console.log('sending data to:' + this.urlRoot);		
		},

		defaults: {			
			"id": null, 
			"mealType": null, 
			"location": null,
			"latitude": null,
			"longitude" : null,
			"mealTime" : null,
			"filled" : null,
			"user_id" : null
	    }
	});

	UTT.Collections.RequestCollection = Backbone.Collection.extend({
		model 	: UTT.Models.MeetAndEatRequest,
		url 	: '/meetrequests'
	});


	//Proposal Model and Collection
	UTT.Models.MeetAndEatProposal = Backbone.Model.extend({		//Extends on Backbone Model to create Custom Model

		urlRoot : '/userlist',

		initialize: function(){	
			console.log('sending data to:' + this.urlRoot);		
		},

		defaults: {			
			"id": null, 
			"filled": null, 
			"user_proposed_to": null,
			"user_proposed_from": null,
			"request_id" : null
	    }
	});

	UTT.Collections.ProposalCollection = Backbone.Collection.extend({
		model 	: UTT.Models.MeetAndEatProposal,
		url 	: '/restaurants'
	});


	//Meal Date Model and Collection
	UTT.Models.MeetAndEatDate = Backbone.Model.extend({		//Extends on Backbone Model to create Custom Model

		urlRoot : '/restaurants',

		initialize: function(){	
			console.log('sending data to:' + this.urlRoot);		
		},

		defaults: {			
			"id": null, 
			"user_1": null, 
			"user_2": null,
			"restaurant_name": null,
			"restaurant_address" : null,
			"meal_time" : null
	    }
	});

	UTT.Collections.MealDateCollection = Backbone.Collection.extend({
		model 	: UTT.Models.MeetAndEatDate,
		url 	: '/restaurants'
	});

}(document, this, jQuery, Backbone, _));