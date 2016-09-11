$(document).ready(function() {
  $("#login-form-error").hide();
  $("#modal-login-form").submit(function() {
    event.preventDefault();
    $.post($(this).attr("action"), $("#modal-login-form").serialize(), function(data) {
      var error = "noErrors";
      switch (data) {
        case "alreadyLogIn":
          error = "Вы уже авторизованы.";
          break;
        case "userNotActive":
          error = "Пользователь не активен.";
          break;
        case "wrongPassOrLogin":
          error = "Неверный логин или пароль.";
          break;
        case "success":
          location.reload();
          break;
      }
      if (error != "noErrors") {
        $("#login-form-error").show();
        $("#login-form-error").text(error);
      }
    });
  });
});