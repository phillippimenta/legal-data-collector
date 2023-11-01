import requests

# Request URL
url = 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam;jsessionid2=poELWaeqnkt3UJZ9VQB6A-aneYCTyE5p2Gjwz-JF.svlpje21g15'

# Headers
headers = {
    'Content-Type': 'multipart/form-data',
    'Cookie': 'JSESSIONID2=poELWaeqnkt3UJZ9VQB6A-aneYCTyE5p2Gjwz-JF.svlpje21g15; PJECSID=6933531b90fdead9; ak_bmsc=B85D17994F0429CAA52837D0D8CA525B~000000000000000000000000000000~YAAQj+UlF9e8rYeLAQAA8AAsiBVYzS3CNx4Tw5ebUYSxVdvvekd4VIqbn2SgSId1e/7Ji3EoYpFDwgYUWHGe0hkT9hU0hSUMVBNvzMNycCifUmgQba9t0uSQ9uy7goKnrl33nEuwixJPG+qLMtPonxT/Ov59z9DDt/2m67203V/Kf5juMQCEi4cEJSfQ1vOyMsO2G0BAf/wgW+Yb4vqR6X4Vy0oSnhVRgrVPf3Zhdwhr9Rf1NFC+VZE5FjS7A554XbCQ/EoOa3yRJY+vmHdc+BrNDJeJ7tDZk92YoIZ7RK8p3+OouUPnsuTvUQX8j8lNPfc/aXl2T1EOpoq/Db9uij87IpMdW3wfOluqSfRvWcr4C/DufX+o2y/VTIHchpBUco9wAKxj8ISTjD9bST/a87leO7VbbqhA4niJlI8niKKxuSxbt6tlLejOu0EnO6UY64ihQlso+42IsVvrDwTToy/Jn/B/iH89jJpnphxcpraA24iQ/JmOmYn7md2RzZgCTxT8sW3COFEjbW5/j/HG0gW3UzlKdVPXQ/c=; bm_sv=2EE930F890070264104954F1F459D5DB~YAAQheUlF/H8um2LAQAAN7c9iBUg0IVhxCGdbKWdxoFKmRZ9tkZ6BhxGivX6NfU6FooCdJVz5rtakvPOi2EI7jtIjViocondtY04RwYovGi8/juTR44ti/ktrWOMciTBhvzJoGzW+v1QRfjK/eeN9fKNmbCPLgDRSm38YkEEkD0YAMwa5CE5XmWPQF2WILh+pESHgBgJv4FOGQOYTLMLNUoVtfX6caZM++Xu+hNn33Og8DMATtX+3CQhZgAAvsHRfw==~1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

processNumber = ''

# Form parameters
data = {
    'AJAXREQUEST': '_viewRoot',
    'fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso': processNumber,
    'mascaraProcessoReferenciaRadio': 'on',
    'fPP:j_id147:processoReferenciaInput': '',
    'fPP:dnp:nomeParte': '',
    'fPP:j_id165:nomeAdv': '',
    'fPP:j_id174:classeProcessualProcessoHidden': '',
    'tipoMascaraDocumento': 'on',
    'fPP:dpDec:documentoParte': '',
    'fPP:Decoration:numeroOAB': '',
    'fPP:Decoration:j_id209': '',
    'fPP:Decoration:estadoComboOAB': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
    'fPP': 'fPP',
    'autoScroll': '',
    'javax.faces.ViewState': 'j_id1',
    'fPP:j_id215': 'fPP:j_id215',
    'AJAX:EVENTS_COUNT': '1'
}

# Make a POST request
response = requests.post(url, headers=headers, data=data)

# Check the response
print(response.text)
