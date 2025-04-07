bl_info = {
    "name": "动画编辑区快速切换",
    "author": "Canta Tam",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "description": "动画摄影表/时间线/曲线编辑器/驱动器/非线性动画编辑区之间更快速的切换",
    "category": "UI",
}

import bpy

# 新增：插件偏好设置类
class MULTIEDITOR_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__  # 使用当前模块名作为标识

    # 添加两个布尔属性
    show_header_buttons: bpy.props.BoolProperty(
        name="标题栏快捷按钮",
        default=True,
        description="开启后,动画编辑区域标题会新添加五个快速切换编辑模式的按钮."
    )
    
    show_context_menu: bpy.props.BoolProperty(
        name="右击快捷菜单",
        default=True,
        description="开启后,Alt+右键，可以在动画编辑区域调出快速切换编辑模式的菜单."
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "show_header_buttons")
        layout.prop(self, "show_context_menu")

# 定义五个不同的操作符（保持不变）
class MULTIEDITOR_OT_CircleButton1(bpy.types.Operator):
    """编辑场景中的所有关键帧."""
    bl_idname = "multieditor.circle_button_1"
    bl_label = "动画摄影表"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.area.type != 'DOPESHEET_EDITOR':
            bpy.ops.screen.space_type_set_or_cycle(space_type='DOPESHEET_EDITOR')
        if hasattr(context.space_data, 'mode'):
            context.space_data.mode = 'DOPESHEET'
        self.report({'INFO'}, "动画摄影表")
        return {'FINISHED'}

class MULTIEDITOR_OT_CircleButton2(bpy.types.Operator):
    """时间线及回放控制."""
    bl_idname = "multieditor.circle_button_2"
    bl_label = "时间线"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.area.type != 'DOPESHEET_EDITOR':
            bpy.ops.screen.space_type_set_or_cycle(space_type='DOPESHEET_EDITOR')
        if hasattr(context.space_data, 'mode'):
            context.space_data.mode = 'TIMELINE'
        self.report({'INFO'}, "时间线")
        return {'FINISHED'}

class MULTIEDITOR_OT_CircleButton3(bpy.types.Operator):
    """对显示为二维曲线的动画/关键帧进行编辑."""
    bl_idname = "multieditor.circle_button_3"
    bl_label = "曲线编辑器"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.area.type != 'GRAPH_EDITOR':
            bpy.ops.screen.space_type_set_or_cycle(space_type='GRAPH_EDITOR')
        if hasattr(context.space_data, 'mode'):
            context.space_data.mode = 'FCURVES'
        self.report({'INFO'}, "曲线编辑器")
        return {'FINISHED'}

class MULTIEDITOR_OT_CircleButton4(bpy.types.Operator):
    """编辑驱动器."""
    bl_idname = "multieditor.circle_button_4"
    bl_label = "驱动器"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.area.type != 'GRAPH_EDITOR':
            bpy.ops.screen.space_type_set_or_cycle(space_type='GRAPH_EDITOR')
        if hasattr(context.space_data, 'mode'):
            context.space_data.mode = 'DRIVERS'
        self.report({'INFO'}, "驱动器")
        return {'FINISHED'}

class MULTIEDITOR_OT_CircleButton5(bpy.types.Operator):
    """动作合并与分层."""
    bl_idname = "multieditor.circle_button_5"
    bl_label = "非线性动画"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NLA_EDITOR')
        self.report({'INFO'}, "非线性动画")
        return {'FINISHED'}


# 操作类（保持不变）
# -----------------------------------------------
class ANIMATION_OT_dopesheet_mode(bpy.types.Operator):
    """编辑场景中的所有关键帧."""
    bl_idname = "animation.dopesheet_mode"
    bl_label = "动画摄影表"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if context.area.type != 'DOPESHEET_EDITOR_EDITOR':
            bpy.ops.screen.space_type_set_or_cycle(space_type='DOPESHEET_EDITOR')
        if hasattr(context.space_data, 'mode'):
            context.space_data.mode = 'DOPESHEET'
        self.report({'INFO'}, "动画摄影表")
        return {'FINISHED'}

class ANIMATION_OT_timeline_mode(bpy.types.Operator):
    """时间线及回放控制."""
    bl_idname = "animation.timeline_mode"
    bl_label = "时间线"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='DOPESHEET_EDITOR')
        context.space_data.mode = 'TIMELINE'
        self.report({'INFO'}, "时间线")
        return {'FINISHED'}

class ANIMATION_OT_grapheditor_mode(bpy.types.Operator):
    """对显示为二维曲线的动画/关键帧进行编辑."""
    bl_idname = "animation.grapheditor_mode"
    bl_label = "曲线编辑器"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='GRAPH_EDITOR')
        context.space_data.mode = 'FCURVES'
        self.report({'INFO'}, "曲线编辑器")
        return {'FINISHED'}
    
class ANIMATION_OT_drivers_mode(bpy.types.Operator):
    """编辑驱动器."""
    bl_idname = "animation.drivers_mode"
    bl_label = "驱动器"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='GRAPH_EDITOR')
        context.space_data.mode = 'DRIVERS'
        self.report({'INFO'}, "驱动器")
        return {'FINISHED'}
    
class ANIMATION_OT_nonlinearanimation_mode(bpy.types.Operator):
    """动作合并与分层."""
    bl_idname = "animation.nonlinearanimation_mode"
    bl_label = "非线性动画"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NLA_EDITOR')
        self.report({'INFO'}, "非线性动画")
        return {'FINISHED'}

# -----------------------------------------------
# 菜单类（保持不变）
# -----------------------------------------------
class ANIMATION_MT_menu(bpy.types.Menu):
    bl_label = "动画编辑快速切换"
    bl_idname = "ANIMATION_MT_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("animation.dopesheet_mode", text="动画摄影表", icon='ACTION')
        layout.operator("animation.timeline_mode", text="时间线", icon='TIME')
        layout.operator("animation.grapheditor_mode",text="曲线编辑器",icon='GRAPH')
        layout.operator("animation.drivers_mode",text="驱动器",icon='DRIVER')
        layout.operator("animation.nonlinearanimation_mode",text="非线性动画",icon='NLA')

# -----------------------------------------------
# 右键菜单触发类（保持不变）
# -----------------------------------------------
class WM_OT_alt_right_click_menu(bpy.types.Operator):
    bl_idname = "wm.alt_right_click_menu"
    bl_label = "Alt+右键菜单"

    def invoke(self, context, event):
        if context.preferences.addons[__name__].preferences.show_context_menu:
            bpy.ops.wm.call_menu(name="ANIMATION_MT_menu")
        return {'FINISHED'}

# 目标编辑器类型列表（保持不变）
TARGET_EDITORS = [
    'DOPESHEET_EDITOR',
    'GRAPH_EDITOR',
    'NLA_EDITOR'
]

draw_handlers = []

addon_keymaps = []

editors = [
    ("Dopesheet", "DOPESHEET_EDITOR"),
    ("Graph Editor", "GRAPH_EDITOR"), 
    ("NLA Editor", "NLA_EDITOR")
]

def draw_buttons(self, context):
    if context.area.type in TARGET_EDITORS and context.preferences.addons[__name__].preferences.show_header_buttons:
        layout = self.layout
        row = layout.row(align=True)

        current_space = context.space_data
        current_type = context.area.type
        current_mode = getattr(current_space, 'mode', None)

        highlight1 = (current_type == 'DOPESHEET_EDITOR' and current_mode == 'DOPESHEET')
        highlight2 = (current_type == 'DOPESHEET_EDITOR' and current_mode == 'TIMELINE')
        highlight3 = (current_type == 'GRAPH_EDITOR' and current_mode == 'FCURVES')
        highlight4 = (current_type == 'GRAPH_EDITOR' and current_mode == 'DRIVERS')
        highlight5 = (current_type == 'NLA_EDITOR')

        row.operator(MULTIEDITOR_OT_CircleButton1.bl_idname, text="", icon='ACTION', depress=highlight1)
        row.operator(MULTIEDITOR_OT_CircleButton2.bl_idname, text="", icon='TIME', depress=highlight2)
        row.operator(MULTIEDITOR_OT_CircleButton3.bl_idname, text="", icon='GRAPH', depress=highlight3)
        row.operator(MULTIEDITOR_OT_CircleButton4.bl_idname, text="", icon='DRIVER', depress=highlight4)
        row.operator(MULTIEDITOR_OT_CircleButton5.bl_idname, text="", icon='NLA', depress=highlight5)

def register():
    # 先注册偏好设置类
    bpy.utils.register_class(MULTIEDITOR_Preferences)
    
    # 注册操作符类
    classes = [
        MULTIEDITOR_OT_CircleButton1,
        MULTIEDITOR_OT_CircleButton2,
        MULTIEDITOR_OT_CircleButton3,
        MULTIEDITOR_OT_CircleButton4,
        MULTIEDITOR_OT_CircleButton5
    ]
    for cls in classes:
        bpy.utils.register_class(cls)

    # 注册头部绘制函数
    header_types = [
        bpy.types.DOPESHEET_HT_header,
        bpy.types.GRAPH_HT_header,
        bpy.types.NLA_HT_header
    ]
    
    global draw_handlers
    for header in header_types:
        header.prepend(draw_buttons)
        draw_handlers.append(header)

    bpy.utils.register_class(ANIMATION_OT_dopesheet_mode)
    bpy.utils.register_class(ANIMATION_OT_timeline_mode)
    bpy.utils.register_class(ANIMATION_OT_grapheditor_mode)
    bpy.utils.register_class(ANIMATION_OT_drivers_mode)
    bpy.utils.register_class(ANIMATION_OT_nonlinearanimation_mode)
    bpy.utils.register_class(ANIMATION_MT_menu)
    bpy.utils.register_class(WM_OT_alt_right_click_menu)

    wm = bpy.context.window_manager
    
    for name, space_type in editors:
        km = wm.keyconfigs.addon.keymaps.new(name=name, space_type=space_type)
        kmi = km.keymap_items.new(WM_OT_alt_right_click_menu.bl_idname, 'RIGHTMOUSE', 'PRESS', alt=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # 注销头部绘制函数
    global draw_handlers
    for header in draw_handlers:
        if draw_buttons in header._dyn_ui_initialize():
            header.remove(draw_buttons)

    # 注销操作符类
    classes = [
        MULTIEDITOR_OT_CircleButton1,
        MULTIEDITOR_OT_CircleButton2,
        MULTIEDITOR_OT_CircleButton3,
        MULTIEDITOR_OT_CircleButton4,
        MULTIEDITOR_OT_CircleButton5
    ]
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    # 注销偏好设置类
    bpy.utils.unregister_class(MULTIEDITOR_Preferences)
    draw_handlers.clear()

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(WM_OT_alt_right_click_menu)
    bpy.utils.unregister_class(ANIMATION_MT_menu)
    bpy.utils.unregister_class(ANIMATION_OT_dopesheet_mode)
    bpy.utils.unregister_class(ANIMATION_OT_timeline_mode)
    bpy.utils.unregister_class(ANIMATION_OT_grapheditor_mode)
    bpy.utils.unregister_class(ANIMATION_OT_drivers_mode)
    bpy.utils.unregister_class(ANIMATION_OT_nonlinearanimation_mode)

if __name__ == "__main__":
    register()
