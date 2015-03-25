$(document).ready(function(){
  $("button.reach_test").click(function(){
      var id=$(this).closest("tr").find('td:eq(2)').text();

      // $.get("/firewalltest",function(data, status){
      //   alert(data +  status);
      // });
      // $(this).html("<i class='fa fa-spinner'></i>")
      $.post("/firewalltest/",{ name : id}, function(data, status)
      {
        if(data["msg"]=="True"){
          // $(".alert").toggleClass('hidden')
          alert("This connection to " + id + " Succeeded");
        }else{
          alert("This connection to " + id + " Failed");
        }


      });

      // $.get("/firewalltest/",function(data, status){alert(data["msg"] + status);});

  });


});
