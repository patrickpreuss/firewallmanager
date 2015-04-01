$(document).ready(function(){
  $('#example').DataTable();
  $("#example1_filter").append($(".dataTables_length"));
  $("#rule-table").DataTable();
  $("body").on("click","button.reach_test",
    function(){
      var id=$(this).closest("tr").find('td:eq(2)').text();
      var parentButton=$(this);
      console.log(parentButton);

      $(this).html('<i class="fa fa-cog fa-spin"></i>');

      $.post("/firewalltest/",{ name : id}, function(data, status)
      {
        parentButton.html('<i class="fa fa-play"></i>')
        console.log(status)
        if(data["msg"]=="True")
        {
          alert("This connection to " + id + " Succeeded");
        }
        else
        {
          alert("This connection to " + id + " Failed");
        }

      });
  });
});

// $(document).ready(function(){
//
//   $("body").on("click","button.reach_test",function(){
//     console.log("Click Activated")
//   })
// })
