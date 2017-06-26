/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/aldryn/aldryn-boilerplate-bootstrap3
 */

// #############################################################################
// CKEDITOR
/**
 * Default CKEDITOR Styles
 * Added within src/settings.py CKEDITOR_SETTINGS.stylesSet
 *
 * @module CKEDITOR
 */
/* global CKEDITOR */

CKEDITOR.allElements = ['p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div'];
CKEDITOR.stylesSet.add('default', [
    /* Block Styles */
    { 'name': 'Текст - Ведущий', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'lead' }},
    { 'name': 'Текст - По левому краю', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'text-left' }},
    { 'name': 'Текст - По центру', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'text-center' }},
    { 'name': 'Текст - По правому краю', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'text-right' }},
    { 'name': 'Текст - По ширине', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'text-justify' }},
    { 'name': 'Текст NoWrap', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'text-nowrap' }},

    { 'name': 'Размер - h1', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'font-size-h1' }},
    { 'name': 'Размер - h2', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'font-size-h2' }},
    { 'name': 'Размер - h3', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'font-size-h3' }},
    { 'name': 'Размер - h4', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'font-size-h4' }},
    { 'name': 'Размер - h5', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'font-size-h5' }},
    { 'name': 'Размер - h6', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'font-size-h6' }},

    { 'name': 'Разделитель', 'element': 'div', 'attributes': { 'class': 'spacer' }},
    { 'name': 'Разделитель - Малый', 'element': 'div', 'attributes': { 'class': 'spacer-xs' }},
    { 'name': 'Разделитель - Большой', 'element': 'div', 'attributes': { 'class': 'spacer-lg' }},
    { 'name': 'Разделитель - Нулевой', 'element': 'div', 'attributes': { 'class': 'spacer-zero' }},

    { 'name': 'Список - без стиля', 'element': ['ul', 'ol'], 'attributes': { 'class': 'list-unstyled' }},
    { 'name': 'Список - в одну строчку', 'element': ['ul', 'ol'], 'attributes': { 'class': 'list-inline' }},
    { 'name': 'Горизонтальное описание', 'element': 'dl', 'attributes': { 'class': 'dl-horizontal' }},

    { 'name': 'Таблица - Без оформления', 'element': 'table', 'attributes': { 'class': 'table-basic' }},
    { 'name': 'Таблица - Базовое оформление', 'element': 'table', 'attributes': { 'class': 'table' }},
    // { 'name': 'Таблица - Адаптивная', 'element': 'table', 'attributes': { 'class': 'table-responsive' }},
    { 'name': 'Таблица - В полосочку', 'element': 'table', 'attributes': { 'class': 'table-striped' }},
    { 'name': 'Таблица - Окаймлённая', 'element': 'table', 'attributes': { 'class': 'table-bordered' }},
    { 'name': 'Таблица - C подсветкой', 'element': 'table', 'attributes': { 'class': 'table-hover' }},
    { 'name': 'Таблица - Компактная', 'element': 'table', 'attributes': { 'class': 'table-condensed' }},

    { 'name': 'Ячейка таблицы - Active', 'element': ['tr', 'th', 'td'], 'attributes': { 'class': 'active' }},
    { 'name': 'Ячейка таблицы - Success', 'element': ['tr', 'th', 'td'], 'attributes': { 'class': 'success' }},
    { 'name': 'Ячейка таблицы - Warning', 'element': ['tr', 'th', 'td'], 'attributes': { 'class': 'warning' }},
    { 'name': 'Ячейка таблицы - Danger', 'element': ['tr', 'th', 'td'], 'attributes': { 'class': 'danger' }},
    { 'name': 'Ячейка таблицы - Info', 'element': ['tr', 'th', 'td'], 'attributes': { 'class': 'info' }},

    /* Inline Styles */
    // { 'name': 'Текст - Primary', 'element': 'span', 'attributes': { 'class': 'text-primary' }},
    // { 'name': 'Текст - Success', 'element': 'span', 'attributes': { 'class': 'text-success' }},
    // { 'name': 'Текст - Info', 'element': 'span', 'attributes': { 'class': 'text-info' }},
    // { 'name': 'Текст - Warning', 'element': 'span', 'attributes': { 'class': 'text-warning' }},
    // { 'name': 'Текст - Danger', 'element': 'span', 'attributes': { 'class': 'text-danger' }},
    // { 'name': 'Текст - Muted', 'element': 'span', 'attributes': { 'class': 'text-muted' }},

    { 'name': 'Изображение - Адаптивное', 'element': 'img', 'attributes': { 'class': 'img-responsive' }},
    { 'name': 'Изображение - Скруглённые углы', 'element': 'img', 'attributes': { 'class': 'img-rounded' }},
    { 'name': 'Изображение - В круге', 'element': 'img', 'attributes': { 'class': 'img-circle' }},
    { 'name': 'Изображение - Тамбнейл', 'element': 'img', 'attributes': { 'class': 'img-thumbnail' }},

    { 'name': 'Прижать к левому краю', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'pull-left' }},
    { 'name': 'Прижать к правому краю', 'element': CKEDITOR.allElements, 'attributes': { 'class': 'pull-right' }},

    { 'name': 'Блок цитирования (прав.)', 'element': 'blockquote', 'attributes': { 'class': 'blockquote-reverse' }}
]);

/*
 * Extend ckeditor default settings
 * DOCS: http://docs.ckeditor.com/#!/api/CKEDITOR.dtd
 */
CKEDITOR.dtd.$removeEmpty.span = 0;
// CKEDITOR.config.autoParagraph = false;

CKEDITOR.on( 'dialogDefinition', function( ev ) {
    var dialogName = ev.data.name;
    var dialogDefinition = ev.data.definition;

    if ( dialogName == 'table' ) {
        var info = dialogDefinition.getContents( 'info' );

        // info.get( 'txtWidth' )[ 'default' ] = '100%';       // Set default width to 100%
        info.get( 'txtBorder' )[ 'default' ] = '0';         // Set default border to 0
    }
});

CKEDITOR.replace( 'editor1' );
