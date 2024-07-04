def getContentData(request, rowData, form_class):
    session = request.session.get('form_data', '')
    if session:
        del request.session['form_data']
        type = session.get('type', '')
        form = form_class(
            data=session.get('form', ''), instance=rowData)
        form._error = session.get('errors', {})
    else:
        form = form_class(instance=rowData)

    return form
