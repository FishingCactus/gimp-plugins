#!/usr/bin/env python

# GIMP Python plug-in template.

from gimpfu import *

def convert(image, layer):
    gimp.progress_init("Cropping image..")

    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(image)

    # Do stuff here.
    next_guide = pdb.gimp_image_find_next_guide(image, 0)
    # horizontal, vertical
    guides = [[], []]
    while next_guide != 0:
        orientation = pdb.gimp_image_get_guide_orientation(image, next_guide)
        guides[orientation].append(pdb.gimp_image_get_guide_position(image, next_guide))
        next_guide = pdb.gimp_image_find_next_guide(image, next_guide)

    if len(guides[0]) == 3 and len(guides[1]) == 3:

        guides[0].sort()
        guides[1].sort()

        pdb.gimp_image_select_rectangle(image, 2, 0, guides[0][1], pdb.gimp_image_width(image) ,(guides[0][2] - guides[0][1]))
        pdb.gimp_image_select_rectangle(image, 0, guides[1][1], 0, (guides[1][2] - guides[1][1]) ,pdb.gimp_image_height(image))

        drawable = pdb.gimp_image_get_active_drawable(image)
        pdb.gimp_edit_clear(drawable)

        pdb.gimp_image_select_rectangle(image, 2, 0, guides[0][2], pdb.gimp_image_width(image) ,(pdb.gimp_image_height(image) - guides[0][2]))
        non_empty = pdb.gimp_edit_cut(drawable)
        floating_sel = pdb.gimp_edit_paste(drawable, False)
        pdb.gimp_layer_translate(floating_sel, 0, - (guides[0][2] - guides[0][1]))
        layer = pdb.gimp_image_merge_down(image, floating_sel, 1)

        drawable = pdb.gimp_image_get_active_drawable(image)

        pdb.gimp_image_select_rectangle(image, 2, guides[1][2], 0, (pdb.gimp_image_width(image) - guides[1][2]) ,pdb.gimp_image_height(image))
        non_empty = pdb.gimp_edit_cut(drawable)
        floating_sel = pdb.gimp_edit_paste(drawable, False)
        pdb.gimp_layer_translate(floating_sel, - (guides[1][2] - guides[1][1]), 0)
        layer = pdb.gimp_image_merge_down(image, floating_sel, 1)

        drawable = pdb.gimp_image_get_active_drawable(image)
        pdb.plug_in_autocrop(image, drawable)

    else:
        pdb.gimp_message("You need exactly 3 horizontal and 3 vertical guides for this plugin")

    # Close the undo group.
    pdb.gimp_undo_push_group_end(image)

register(
    "python_fu_background_to_border_image",
    "Convert background to border image",
    "Ment for web development. Where you want to convert a background_image to a border_image ( and create a 9slice )",
    "Pieter Vantorre",
    "Fishing Cactus",
    "2016",
    "<Image>/Filters/Web/Background To Border Image",
    "*",      # Alternately use RGB, RGB*, GRAY*, INDEXED etc.
    [],
    [
         (PF_TEXT, "text", "Some Text")
    ],
    convert)

main()
