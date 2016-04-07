(function (document, window, $, Backbone, _){


	UTT.Views.Home = Backbone.View.extend({

		className : "row",

		initialize : function(){
			this.render();
		},

		collection : new UTT.Collections.RestaurantCollection(),

		render : function(){		
			$(this.el).html(this.template());				
			restaurantBody = this.$el.find("#reviewBody")
			this.collection.fetch({
				success : function(model, response){
					console.log(response)
					$.each(response.restaurants, function(index, data){
						$(restaurantBody).append(new UTT.Views.Restaurant({model:data}).el);
					})
				},
				error: function(model, response){
					console.log(response);
				}
			});
			return this;
		},

		events : {			
			"submit #resturant-form"	: "addRestaurant",
			"submit #updateRestaurant"	: "deleteRestaurant"		
		},

		addRestaurant : function(){
			var data =  this.getFormData(),
			that = this,
			resturant = new UTT.Models.RestaurantModel();
			console.log(data);
			if(!_.isEmpty(data)){
				resturant.save(data,{
					success:function(model, response){							
						that.collection.add(response);
					  	that.render();
					},
					error : function(model, response){						
						window.aelrt("Error Processing")								
					}
				});	
			}else{
				window.alert("Empty form");
			}
			return false;
		},

		getFormData : function(){			
			var data = {},
			form = this.$el.find("#resturant-form"),
			viewArr = form.serializeArray(),
			valid = true;			

			$.each(viewArr, function(i,d){
				data[viewArr[i].name] = viewArr[i].value;
				if(viewArr[i].value === "") valid = false;
			});		
			if(valid){
				return data;
			}else{
				return {};
			}
		}

	});

	UTT.Views.Request = Backbone.View.extend({

		className : "row",

		initialize : function(){
			this.render();
		},

		collection : new UTT.Collections.RequestCollection(),

		render : function(){		
			$(this.el).html(this.template());				
			reqBody = this.$el.find("#reviewBody")
			this.collection.fetch({
				success : function(model, response){
					console.log(response)
					$.each(response.allrequests, function(index, data){
						$(reqBody).append(new UTT.Views.RequestList({model:data}).el);
					})
				},
				error: function(model, response){
					console.log(response);
				}
			});
			return this;
		},

		events : {			
			"submit #mealRequest-form"	: "addNewMeetingRequest"			
		},

		addNewMeetingRequest : function(){
			var data =  this.getFormData(),
			that = this,
			newRequest = new UTT.Models.MeetAndEatRequest();
			console.log(data);
			if(!_.isEmpty(data)){
				window.alert("About to Save")
				newRequest.save(data,{
					success:function(model, response){							
						that.collection.add(response);
					  	that.render();
					},
					error : function(model, response){						
						window.alert("Error Processing")

					}
				});	
			}else{
				window.alert("Empty form");
			}
			return false;
		},

		getFormData : function(){			
			var data = {},
			form = this.$el.find("#mealRequest-form"),
			viewArr = form.serializeArray(),
			valid = true;			

			$.each(viewArr, function(i,d){
				data[viewArr[i].name] = viewArr[i].value;
				if(viewArr[i].value === "") valid = false;
			});		
			if(valid){
				return data;
			}else{
				return {};
			}
		}

	});


	UTT.Views.User = Backbone.View.extend({

		className : "row",

		initialize : function(){
			this.render();
		},

		collection : new UTT.Collections.UserCollection(),

		render : function(){		
			$(this.el).html(this.template());				
			userBody = this.$el.find("#reviewBody")
			this.collection.fetch({
				success : function(model, response){
					console.log(response)
					$.each(response.users, function(index, data){
						$(userBody).append(new UTT.Views.UserList({model:data}).el);
					})
				},
				error: function(model, response){
					console.log(response);
				}
			});
			return this;
		},

		events : {			
			"submit #addUser-form"	: "addNewUser"			
		},

		addNewUser : function(){
			var data =  this.getFormData(),
			that = this,
			newUser = new UTT.Models.MeetAndEatUser();
			console.log(data);
			if(!_.isEmpty(data)){
				newUser.save(data,{
					success:function(model, response){							
						that.collection.add(response);
					  	that.render();
					},
					error : function(model, response){						
						window.aelrt("Error Processing")								
					}
				});	
			}else{
				window.alert("Empty form");
			}
			return false;
		},

		getFormData : function(){			
			var data = {},
			form = this.$el.find("#addUser-form"),
			viewArr = form.serializeArray(),
			valid = true;			

			$.each(viewArr, function(i,d){
				data[viewArr[i].name] = viewArr[i].value;
				if(viewArr[i].value === "") valid = false;
			});		
			if(valid){
				return data;
			}else{
				return {};
			}
		}

	});


	
	//View for RequestList.html template
	UTT.Views.RequestList = Backbone.View.extend({

		className : "row reqBody",

		initialize : function(){
			this.render();
		},

		render : function(){		
			$(this.el).html(this.template(this.model));	
			return this;
		}

	});

	//View for Restaurant.html template
	UTT.Views.Restaurant = Backbone.View.extend({

		className : "row restaurantBody",

		initialize : function(){
			this.render();
		},

		render : function(){		
			$(this.el).html(this.template(this.model));	
			return this;
		}

	});

	//View for UserList.html template
	UTT.Views.UserList = Backbone.View.extend({

		className : "row userBody",

		initialize : function(){
			this.render();
		},

		render : function(){		
			$(this.el).html(this.template(this.model));	
			return this;
		}

	});


	
}(document, this, jQuery, Backbone, _));