CKEDITOR.on("instanceReady", function (ev) {
  const editorContainer = ev.editor.container.$;
  editorContainer.style.border = "2px solid #ffc107";
  editorContainer.style.borderRadius = "10px";
  editorContainer.style.boxShadow = "0 0 5px rgba(0,0,0,0.1)";
  editorContainer.style.padding = "0";
  editorContainer.style.backgroundColor = "#fff";

  const frame = editorContainer.querySelector(".cke_wysiwyg_frame");
  if (frame) {
    frame.style.height = "300px";
    frame.style.borderRadius = "10px";
    frame.style.border = "none";
  }

  const toolbar = editorContainer.querySelector(".cke_top");
  if (toolbar) {
    toolbar.style.backgroundColor = "#f1f1f1";
    toolbar.style.borderBottom = "2px solid #ffc107";
    toolbar.style.borderRadius = "10px 10px 0 0";
    toolbar.style.padding = "10px";
  }
});
