
  function newBtnClicked(){
      var newbtn = document.getElementById("admin-blog-new-btn");
      var editbtn = document.getElementById("admin-blog-edit-btn");
      var deletebtn = document.getElementById("admin-blog-delete-btn");
      var newSection = document.getElementById("new-blog-section");
      var editSection = document.getElementById("edit-blog-section");
      var deleteSection = document.getElementById("delete-blog-section");

      newbtn.classList.add("bg-success" , "text-light");
      editbtn.classList.remove("bg-success" , "text-light");
      deletebtn.classList.remove("bg-success" , "text-light");
      newSection.style.display = "block";
      editSection.style.display = "none";
      deleteSection.style.display = "none";
  }
    function editBtnClicked(){
      var newbtn = document.getElementById("admin-blog-new-btn");
      var editbtn = document.getElementById("admin-blog-edit-btn");
      var deletebtn = document.getElementById("admin-blog-delete-btn");
      var newSection = document.getElementById("new-blog-section");
      var editSection = document.getElementById("edit-blog-section");
      var deleteSection = document.getElementById("delete-blog-section");

      editbtn.classList.add("bg-success" , "text-light");
      newbtn.classList.remove("bg-success" , "text-light");
      deletebtn.classList.remove("bg-success" , "text-light");
      newSection.style.display = "none";
      editSection.style.display = "block";
      deleteSection.style.display = "none";
  }
   function deleteBtnClicked(){
      var newbtn = document.getElementById("admin-blog-new-btn");
      var editbtn = document.getElementById("admin-blog-edit-btn");
      var deletebtn = document.getElementById("admin-blog-delete-btn");
      var newSection = document.getElementById("new-blog-section");
      var editSection = document.getElementById("edit-blog-section");
      var deleteSection = document.getElementById("delete-blog-section");

      deletebtn.classList.add("bg-success" , "text-light");
      newbtn.classList.remove("bg-success" , "text-light");
      editbtn.classList.remove("bg-success" , "text-light");

      newSection.style.display = "none";
      editSection.style.display = "none";
      deleteSection.style.display = "block";
  }
newBtnClicked();
