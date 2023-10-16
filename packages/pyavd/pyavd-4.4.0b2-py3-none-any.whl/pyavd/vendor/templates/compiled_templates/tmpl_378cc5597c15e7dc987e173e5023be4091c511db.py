from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/stun.j2'

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
        yield '!\nstun\n'
        if t_2(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client')):
            pass
            yield '   client\n'
            for l_1_profile in t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client'), 'server_profiles'), 'name'):
                _loop_vars = {}
                pass
                yield '      server-profile '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield '\n'
                if t_2(environment.getattr(l_1_profile, 'ip_address')):
                    pass
                    yield '         ip address '
                    yield str(environment.getattr(l_1_profile, 'ip_address'))
                    yield '\n'
            l_1_profile = missing
        if t_2(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server')):
            pass
            yield '   server\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'local_interface')):
                pass
                yield '      local-interface '
                yield str(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'local_interface'))
                yield '\n'

blocks = {}
debug_info = '7=24&10=27&12=30&13=34&14=36&15=39&19=42&21=45&22=48'