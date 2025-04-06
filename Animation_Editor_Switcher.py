bl_info = {
    "name": "动画编辑区快速切换",
    "author": "Canta Tam",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "Multiple Editors",
    "description": "动画摄影表/时间线/曲线编辑器/驱动器/非线性动画编辑区之间更快速的切换",
    "category": "UI",
}

import bpy

# 定义五个不同的操作符
class MULTIEDITOR_OT_CircleButton1(bpy.types.Operator):
    """编辑场景中的所有关键帧."""
    bl_idname = "multieditor.circle_button_1"
    bl_label = "动画摄影表"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 切换到Dope Sheet并设置模式
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
        # 切换到Timeline
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
        # 切换到Graph Editor并设置模式
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
        # 切换到Drivers模式
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
        # 切换到NLA Editor
        bpy.ops.screen.space_type_set_or_cycle(space_type='NLA_EDITOR')
        self.report({'INFO'}, "非线性动画")
        return {'FINISHED'}

# 目标编辑器类型列表
TARGET_EDITORS = [
    'DOPESHEET_EDITOR',  # Dope Sheet & Timeline
    'GRAPH_EDITOR',      # Graph Editor & Drivers
    'NLA_EDITOR'         # Nonlinear Animation
]

# 存储注册的绘制函数引用
draw_handlers = []

def draw_buttons(self, context):
    if context.area.type in TARGET_EDITORS:
        layout = self.layout
        row = layout.row(align=True)

        # 获取当前编辑器的类型和模式
        current_space = context.space_data
        current_type = context.area.type
        current_mode = getattr(current_space, 'mode', None)

        # 判断高亮条件
        highlight1 = (current_type == 'DOPESHEET_EDITOR' and current_mode == 'DOPESHEET')
        highlight2 = (current_type == 'DOPESHEET_EDITOR' and current_mode == 'TIMELINE')
        highlight3 = (current_type == 'GRAPH_EDITOR' and current_mode == 'FCURVES')
        highlight4 = (current_type == 'GRAPH_EDITOR' and current_mode == 'DRIVERS')
        highlight5 = (current_type == 'NLA_EDITOR')

        # 绘制带高亮状态的按钮
        row.operator(MULTIEDITOR_OT_CircleButton1.bl_idname, text="", icon='ACTION', depress=highlight1)
        row.operator(MULTIEDITOR_OT_CircleButton2.bl_idname, text="", icon='TIME', depress=highlight2)
        row.operator(MULTIEDITOR_OT_CircleButton3.bl_idname, text="", icon='GRAPH', depress=highlight3)
        row.operator(MULTIEDITOR_OT_CircleButton4.bl_idname, text="", icon='DRIVER', depress=highlight4)
        row.operator(MULTIEDITOR_OT_CircleButton5.bl_idname, text="", icon='NLA', depress=highlight5)

def register():
    bpy.utils.register_class(MULTIEDITOR_OT_CircleButton1)
    bpy.utils.register_class(MULTIEDITOR_OT_CircleButton2)
    bpy.utils.register_class(MULTIEDITOR_OT_CircleButton3)
    bpy.utils.register_class(MULTIEDITOR_OT_CircleButton4)
    bpy.utils.register_class(MULTIEDITOR_OT_CircleButton5)

    # 注册到所有目标编辑器的头部
    header_types = [
        bpy.types.DOPESHEET_HT_header,
        bpy.types.GRAPH_HT_header,
        bpy.types.NLA_HT_header
    ]

    global draw_handlers
    for header in header_types:
        header.prepend(draw_buttons)
        draw_handlers.append(header)

def unregister():
    global draw_handlers
    for header in draw_handlers:
        if draw_buttons in header._dyn_ui_initialize():
            header.remove(draw_buttons)

    bpy.utils.unregister_class(MULTIEDITOR_OT_CircleButton1)
    bpy.utils.unregister_class(MULTIEDITOR_OT_CircleButton2)
    bpy.utils.unregister_class(MULTIEDITOR_OT_CircleButton3)
    bpy.utils.unregister_class(MULTIEDITOR_OT_CircleButton4)
    bpy.utils.unregister_class(MULTIEDITOR_OT_CircleButton5)
    draw_handlers.clear()

if __name__ == "__main__":
    register()
