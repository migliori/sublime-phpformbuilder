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
            'addHelper($helper_text, $element_name)',
            'addIcon($input_name, $icon_html, $pos)',
            'addHtml($html, $element_name = \'\', $pos = \'after\')',
            'groupInputs($input1, $input2, $input3 = \'\')',
            'addInputWrapper($html, $element_name)',
            'addInput--function--($type, $name, $value = \'\', $label = \'\', $attr = \'\')',
            'addTextarea($name, $value = \'\', $label = \'\', $attr = \'\')',
            'addOption($select_name, $value, $txt, $group_name = \'\', $attr = \'\')',
            'addSelect($select_name, $label = \'\', $attr = \'\', $displayGroupLabels = true)',
            'addCountrySelect($select_name, $label = \'\', $attr = \'\', $user_options = array())',
            'addRadio($group_name, $label, $value, $attr)',
            'printRadioGroup($group_name, $label = \'\', $inline = true, $attr = \'\')',
            'addCheckbox($group_name, $label, $name, $value, $attr)',
            'printCheckboxGroup($group_name, $label = \'\', $inline = true, $attr = \'\')',
            'addFileUpload($type, $name, $value = \'\', $label = \'\', $attr = \'\', $fileUpload_config = \'\')',
            'centerButtons($center)',
            'addBtn($type, $name, $value, $text, $attr = \'\', $btnGroupName = \'\')',
            'printBtnGroup($btnGroupName, $label = \'\')',
            'addPlugin($plugin_name, $selector, $js_content = \'default\', $js_replacements = \'\')',
            'addRecaptchaV3($sitekey, $action = \'default\', $response_fieldname = \'g-recaptcha-response\', $xml_config = \'default\')',
            'addInvisibleRecaptcha($sitekey)',
            'addRecaptchaV2($sitekey, $recaptcha_id = \'recaptcha\', $center = false)',
            'modal($modal_target)',
            'popover($popover_link)',
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
            'addHelper',
            'addIcon',
            'addHtml',
            'groupInputs',
            'addInputWrapper',
            'addInput--function--',
            'addTextarea',
            'addOption',
            'addSelect',
            'addCountrySelect',
            'addRadio',
            'printRadioGroup',
            'addCheckbox',
            'printCheckboxGroup',
            'addFileUpload',
            'centerButtons',
            'addBtn',
            'printBtnGroup',
            'addPlugin',
            'addRecaptchaV3',
            'addInvisibleRecaptcha',
            'addRecaptchaV2',
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
