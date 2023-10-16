from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/stun.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_stun = resolve('stun')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='stun') if l_0_stun is missing else l_0_stun)):
        pass
        yield '\n## STUN\n'
        if t_2(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client')):
            pass
            yield '\n### STUN Client\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client'), 'server_profiles')):
                pass
                yield '\n#### Server Profiles\n\n| Server Profile | IP address |\n| -------------- | ---------- |\n'
                for l_1_server_profile in t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client'), 'server_profiles'), 'name'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_server_profile, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_server_profile, 'ip_address'))
                    yield ' |\n'
                l_1_server_profile = missing
        if t_2(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server')):
            pass
            yield '\n### STUN Server\n\n| Server local interface |\n| ---------------------- |\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'local_interface')):
                pass
                yield '| '
                yield str(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'local_interface'))
                yield ' |\n'
        yield '\n### STUN Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/stun.j2', 'documentation/stun.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&10=27&13=30&19=33&20=37&24=42&30=45&31=48&38=51'