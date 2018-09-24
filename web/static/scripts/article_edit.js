let articleContent = $("#content").attr('value');

var simplemde = new SimpleMDE({ element: $("#content")[0] });
simplemde.value(articleContent);