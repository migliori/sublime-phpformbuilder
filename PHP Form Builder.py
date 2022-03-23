import sublime, sublime_plugin

class CompletionTriggerCommand(sublime_plugin.TextCommand):
    def run(self, edit, completionTriggerText):
        self.view.insert(edit, self.view.sel()[0].begin(), completionTriggerText)
        self.view.run_command("auto_complete")
        self.view.run_command("insert_best_completion")

class phpFormBuilderCommand(sublime_plugin.TextCommand):
    def on_quick_panel_selection(self, index):
        if index == -1:
            return
        else:
            self.view.run_command('completion_trigger', {"completionTriggerText": self.completions_trigger[index]})
    def run(self, edit):
        self.form_element_labels = [
            'new Form($form_ID, $layout = \'horizontal\', $attr = \'\');',
            'newFormTemplate',
            'setMode($mode);',
            'useLoadJs($bundle = \'\')',
            'setPluginsUrl($url)',
            'setAction($url, $add_get_vars = true)',
            'setMethod($method);',
            'setOptions();',
            'startFieldset($legend = \'\', $fieldset_attr = \'\', $legend_attr = \'\')',
            'endFieldset()',
            'startDependentFields($parent_field, $show_values, $inverted = false)',
            'endDependentFields()',
            'setCols($labelsCols, $fieldsCols, $breakpoint = \'sm\')',
            'addAddon($input_name, $addon_html, $pos))',
            'addHeading($heading_html, $heading_tag, $attr)',
            'addHelper($helper_text, $element_name)',
            'addIcon($input_name, $icon_html, $pos)',
            'addHtml($html, $element_name = \'\', $pos = \'after\')',
            'buildAlert($content_text, $framework, $type)',
            'groupElements($input1, $input2, $input3 = \'\')',
            'addInputWrapper($html, $element_name)',
            'addInput--function--($type, $name, $value = \'\', $label = \'\', $attr = \'\')',
            'addTextarea($name, $value = \'\', $label = \'\', $attr = \'\')',
            'addOption($select_name, $value, $txt, $group_name = \'\', $attr = \'\')',
            'addSelect($select_name, $label = \'\', $attr = \'\', $displayGroupLabels = true)',
            'addCountrySelect($select_name, $label = \'\', $attr = \'\', $user_options = array())',
            'addTimeSelect($select_name, $label = '', $attr = '', $user_options = array())',
            'addRadio($group_name, $label, $value, $attr)',
            'printRadioGroup($group_name, $label = \'\', $inline = true, $attr = \'\')',
            'addCheckbox($group_name, $label, $name, $value, $attr)',
            'printCheckboxGroup($group_name, $label = \'\', $inline = true, $attr = \'\')',
            'addFileUpload($type, $name, $value = \'\', $label = \'\', $attr = \'\', $fileUpload_config = \'\')',
            'centerContent($center = true, $stack = false)',
            'startRow($additionalClass = \'\', $id = \'\')',
            'endRow()',
            'startCol($col_number, $breakpoint = \'sm\', $additionalClass = \'\', $id = \'\')',
            'endCol()',
            'addBtn($type, $name, $value, $text, $attr = \'\', $btnGroupName = \'\')',
            'printBtnGroup($btnGroupName, $label = \'\')',
            'addPlugin($plugin_name, $selector, $js_content = \'default\', $js_replacements = \'\')',
            'addRecaptchaV3($sitekey, $action = \'default\', $response_fieldname = \'g-recaptcha-response\', $xml_config = \'default\')',
            'addHcaptcha($hcaptcha_site_key, $attr)',
            'modal()',
            'popover()',
            'cleanHtmlOutput($html)',
            'render($debug = false)',
            'printIncludes($type)',
            'printJsCode()',
            'Form::testToken($form_ID)',
            'Form::validate($form_ID, $lang = \'en\')',
            'Form::sendMail($from_email, $adress, $subject, $filter_values = \'\', $values = \'\')',
            'Form::registerValues($form_ID)',
            'Form::mergeValues(array(\'step-form-1\', \'step-form-2\', \'step-form-3\'))',
            'Form::clear($form_ID)'
        ]
        self.completions_trigger = [
            'newForm',
            'newFormTemplate',
            'setMode',
            'useLoadJs',
            'setPluginsUrl',
            'setAction',
            'setMethod',
            'setOptions',
            'startFieldset',
            'endFieldset',
            'startDependentFields',
            'endDependentFields',
            'setCols',
            'addAddon',
            'addHeading',
            'addHelper',
            'addIcon',
            'addHtml',
            'buildAlert',
            'groupElements',
            'addInputWrapper',
            'addInput--function--',
            'addTextarea',
            'addOption',
            'addSelect',
            'addCountrySelect',
            'addTimeSelect',
            'addRadio',
            'printRadioGroup',
            'addCheckbox',
            'printCheckboxGroup',
            'addFileUpload',
            'centerContent',
            'startRow',
            'endRow',
            'startCol',
            'endCol',
            'addBtn',
            'printBtnGroup',
            'addPlugin',
            'addRecaptchaV3',
            'addHcaptcha',
            'modal',
            'popover',
            'cleanHtmlOutput',
            'render',
            'printIncludes',
            'printJsCode',
            'FormTestToken',
            'FormValidate',
            'FormSendMail',
            'FormRegisterValues',
            'FormMergeValues',
            'FormClear'
        ]
        self.view.window().show_quick_panel(self.form_element_labels, self.on_quick_panel_selection)
