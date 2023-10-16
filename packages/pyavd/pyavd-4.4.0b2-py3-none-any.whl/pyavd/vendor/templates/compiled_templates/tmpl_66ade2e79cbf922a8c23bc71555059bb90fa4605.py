from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_security = resolve('ip_security')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security)):
        pass
        yield '!\nip security\n'
        for l_1_ike_policy in t_1(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'ike_policies'), []):
            _loop_vars = {}
            pass
            yield '   !\n   ike policy '
            yield str(environment.getattr(l_1_ike_policy, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_ike_policy, 'local_id')):
                pass
                yield '      local_id '
                yield str(environment.getattr(l_1_ike_policy, 'local_id'))
                yield '\n'
        l_1_ike_policy = missing
        for l_1_sa_policy in t_1(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'sa_policies'), []):
            _loop_vars = {}
            pass
            yield '   !\n   sa policy '
            yield str(environment.getattr(l_1_sa_policy, 'name'))
            yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'intergrity')):
                pass
                yield '      esp intergrity '
                yield str(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'intergrity'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'encryption')):
                pass
                yield '      esp encryption '
                yield str(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'encryption'))
                yield '\n'
            if t_2(environment.getattr(l_1_sa_policy, 'pfs_dh_group')):
                pass
                yield '      pfs_dh_group '
                yield str(environment.getattr(l_1_sa_policy, 'pfs_dh_group'))
                yield '\n'
        l_1_sa_policy = missing
        for l_1_profile in t_1(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'profiles'), []):
            _loop_vars = {}
            pass
            yield '   !\n   profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_profile, 'ike_policy')):
                pass
                yield '      ike-policy '
                yield str(environment.getattr(l_1_profile, 'ike_policy'))
                yield '\n'
            if t_2(environment.getattr(l_1_profile, 'sa_policy')):
                pass
                yield '      sa-policy '
                yield str(environment.getattr(l_1_profile, 'sa_policy'))
                yield '\n'
            if t_2(environment.getattr(l_1_profile, 'connection')):
                pass
                yield '      connection '
                yield str(environment.getattr(l_1_profile, 'connection'))
                yield '\n'
            if t_2(environment.getattr(l_1_profile, 'shared_key')):
                pass
                yield '      shared-key 7 '
                yield str(environment.getattr(l_1_profile, 'shared_key'))
                yield '\n'
            if ((t_2(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'interval')) and t_2(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'time'))) and t_2(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'action'))):
                pass
                yield '      dpd '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'interval'))
                yield ' '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'time'))
                yield ' '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'action'))
                yield '\n'
            if t_2(environment.getattr(l_1_profile, 'mode')):
                pass
                yield '      mode '
                yield str(environment.getattr(l_1_profile, 'mode'))
                yield '\n'
        l_1_profile = missing
        if t_2(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller')):
            pass
            yield '   !\n   key controller\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller'), 'profile')):
                pass
                yield '      profile '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller'), 'profile'))
                yield '\n'

blocks = {}
debug_info = '7=24&10=27&12=31&13=33&14=36&17=39&19=43&20=45&21=48&23=50&24=53&26=55&27=58&30=61&32=65&33=67&34=70&36=72&37=75&39=77&40=80&42=82&43=85&45=87&46=90&48=96&49=99&52=102&55=105&56=108'