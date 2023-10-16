function set_service_icon(iframe_id, icon_path) {
  const service_id = iframe_id.slice(iframe_id.indexOf("_") + 1);
  let spinner = $(`#${service_id}`).children("img.spinner");
  spinner.attr("src", icon_path)
  spinner.removeClass("spinner")
}

function logoutSuccess(iframe_id, success_img_path) {
  set_service_icon(iframe_id, success_img_path)
}

function logoutFailure(iframe_id, failure_img_path) {
  set_service_icon(iframe_id, failure_img_path)
}
